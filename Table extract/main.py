import camelot


def main():
    #     here we can pass the cordinates of table find in extract_table_cord function in table areas.
    tables = camelot.read_pdf('test.pdf', pages='69', flavor='stream', table_areas=[
                              '51.0236, 272.31879999999995, 545.9578, 97.8021'])
    tables
    tables
    # <TableList n=1>
    tables.export('foo.csv', f='csv', compress=True)  # json, excel, html
    tables[0]
    tables[0].parsing_report
    {
        'accuracy': 99.02,
        'whitespace': 12.24,
        'order': 1,
        'page': 1
    }
    tables[0].to_csv('foo.csv')  # to_json, to_excel, to_html
    return tables[0].df  # get a pandas DataFrame!


if __name__ == "__main__":
    df = main()
    print(df)
