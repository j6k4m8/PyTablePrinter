
TITLEISH_KEYS = [
    'key',
    'name',
    'title',
    'id'
]

UNION = "union"
INTERSECT = "intersect"


class TablePrinter():

    def __init__(self, data, outsides=True, col_order=None, schema=UNION):
        """
        Initialize with parameters.

        Arguments:
            data (list of dicts): Data to print nicely
            outsides (bool: True): Whether to use | characters on the ouside

        Returns:
            None

        Raises:
            ValueError: If either of the default params are of the wrong type
        """
        self._bar = "|" if outsides else ""
        if type(data) is dict:
            for k, v in data:
                data[k]['key'] = v
            self.data = data.values()
        elif type(data) is list:
            for d in data:
                if type(d) is not dict:
                    raise ValueError("data must be either [\{\},\{\}] or \{\}")
            self.data = data

        if col_order is None:
            self.col_order = [(s, s, None) for s in sorted(data[0].keys())]
        else:
            self.col_order = col_order

        for i in range(len(self.col_order)):
            if type(self.col_order[i]) is not tuple:
                self.col_order[i] = (self.col_order[i], self.col_order[i], None)
            # else:
            #     if hasattr(self.col_order[i][2], '__call__'):
            #

        for n in TITLEISH_KEYS:
            if n in self.col_order:
                self.col_order.remove(n)
                tmp = [n]
                tmp.extend(self.col_order)
                self.col_order = tmp
                break

    def data_is_uniform(self):
        """
        If each item in self.data (array of dicts) has the same schema.

        Arguments:
            None

        Returns:
            bool: All items have the same schema
        """
        base_schema = []
        updates = 0
        for d in self.data:
            for k, v in d.iteritems():
                if k not in base_schema:
                    updates += 1
                    base_schema.append(k)
        return updates == 1

    def to_markdown(self):
        """
        Return a markdown string that can be barfed into a .md file.

        Arguments:
            None

        Returns:
            str: MD representation of the data
        """
        md_out = []
        md_out.append(str(self._bar + " {} " + self._bar)
                      .format("|".join([k[1] for k in self.col_order])))
        md_out.append(str(self._bar + " {} " + self._bar)
                      .format("|".join(["-----"] * len(self.col_order))))

        for d in self.data:
            md_out.append(self._markdown_row(d))
        return "\n".join(md_out)

    def _markdown_row(self, d):
        row = []
        for k in self.col_order:
            if len(k) is 3 and hasattr(k[2], '__call__'):
                # the last item in the tuple is a function
                row.append(str(k[2](d)))
            elif k[0] in d:
                row.append(str(d[k[0]]))
            else:
                row.append("")
        return "| {} |".format('|'.join(row))

    def to_latex(self, hrules="hline"):
        ltx_out = []
        ltx_out.append("\\begin{center}")
        ltx_out.append("\\begin{{tabular}}{{ {} }}".format(" c " * len(self.col_order)))

        for d in self.data:
            ltx_out.append(self._latex_row(d))
        ltx_out.append("\\end{tabular}")
        ltx_out.append("\\end{center}")
        return "\n".join(ltx_out)

    def _latex_row(self, d):
        row = []
        for k in self.col_order:
            if len(k) is 3 and hasattr(k[2], '__call__'):
                row.append(str(k[2](d)))
            elif k[0] in d:
                row.append(str(d[k[0]]))
            else:
                row.append("")
        return " {} ".format(" & ".join(row)) + "\\\\"
