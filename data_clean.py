import csv
import sqlite3 as lite
import json
import pandas as pd


conn = lite.connect('database.db')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS wells')
cur.execute('CREATE TABLE wells (well_number TEXT, quarter TEXT, oil TEXT, gas TEXT, brine TEXT)')


with open('data.csv') as file:
    reader = csv.DictReader(file)

    well_numbers = []

    '''
    'API WELL  NUMBER', 'Production Year','QUARTER 1,2,3,4', 
    'OWNER NAME', 'COUNTY', 'TOWNSHIP', 
    'WELL NAME', 'WELL NUMBER','OIL', 
    'GAS', 'BRINE','DAYS'
    '''
    quarters = []
    for row in reader:
        well_number = row['API WELL  NUMBER']
        if well_number not in well_numbers:
            well_numbers.append(well_number)
        quarter = row['QUARTER 1,2,3,4']
        if quarter not in quarters:
            quarters.append(quarter)
        oil = row['OIL']
        gas = row['GAS']
        brine = row['BRINE']
        cur.execute('INSERT INTO wells VALUES (?,?,?,?,?)', (well_number, quarter, oil, gas, brine))
        conn.commit()
    file.seek(0)
    rows = []
    for row in well_numbers:    
        cur.execute('SELECT OIL,GAS,BRINE FROM wells WHERE well_number = ?', (row,)) 
        rows.append(cur.fetchall())
        
    wells = {}
    for i in range(len(rows)):
        wells[well_numbers[i]] = rows[i]
        print(rows[i])
    
    print(wells)


    


conn.close()



