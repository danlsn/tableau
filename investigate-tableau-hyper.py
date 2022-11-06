from tableauhyperapi import HyperProcess, Connection, TableDefinition, Telemetry, Inserter, CreateMode

with HyperProcess(Telemetry.DO_NOT_SEND_USAGE_DATA_TO_TABLEAU, 'myapp') as hyper:
    with Connection(hyper.endpoint, './extracts/Bechdel Test API x oMDB API.hyper', CreateMode.NONE) as connection:
        con = connection
        hyp = hyper
        print(con.catalog)
        schema = con.catalog.get_schema_names()
        table_def = con.catalog.get_table_names('Extract')
        first_table = table_def[0]
        ft = con.catalog.get_table_definition(first_table)
        cols = ft.columns
        print(len(cols))
        table_name = ft.table_name
        pass

