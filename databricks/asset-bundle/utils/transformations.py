class reusable:
    def dropColumns(self, df, columns):
        return df.drop(*columns)
