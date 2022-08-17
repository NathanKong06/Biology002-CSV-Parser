from csv import DictReader

african_and_dwv = 0
african_and_no_dwv = 0
african_and_no_data = 0
african_and_no_rna = 0

european_and_dwv = 0
european_and_no_dwv = 0
european_and_no_data = 0
european_and_no_rna = 0


no_data_and_dwv = 0
no_data_and_no_dwv = 0
no_data_and_no_data = 0
no_data_and_no_rna = 0

other_and_dwv = 0
other_and_no_dwv = 0
other_and_no_data = 0
other_and_no_rna = 0

african = 0
european = 0
no_data = 0
other = 0

has_dwv = 0
has_no_dwv = 0
no_dwv_data = 0
no_rna = 0




with open('Sheet1.csv', 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    for row in csv_dict_reader:
        if (row['Lineage'] == "African"):
            african = african + 1
        elif (row['Lineage'] == "European"):
            european = european + 1
        elif (row['Lineage'] == "other"):
            other = other + 1
        elif (row['Lineage'] == "no data"):
            no_data = no_data + 1
                        
        if (row['Does the bee have DWV?'] == "has DWV"):
            has_dwv = has_dwv + 1
        elif (row['Does the bee have DWV?'] == "not infected with DWV"):
            has_no_dwv = has_no_dwv + 1
        elif (row['Does the bee have DWV?'] == ""):
            no_dwv_data = no_dwv_data + 1
        elif (row['Does the bee have DWV?'] == "no RNA "):
            no_rna = no_rna + 1
            
        
        if (row['Lineage'] == "African" and row['Does the bee have DWV?'] == "has DWV"):
            african_and_dwv = african_and_dwv + 1
        elif (row['Lineage'] == "African" and row['Does the bee have DWV?'] == "not infected with DWV"):
            african_and_no_dwv = african_and_no_dwv + 1
        elif (row['Lineage'] == "African" and row['Does the bee have DWV?'] == ""):
            african_and_no_data = african_and_no_data + 1   
        elif (row['Lineage'] == "African" and row['Does the bee have DWV?'] == "no RNA "):
            african_and_no_rna = african_and_no_rna + 1     
             
        elif (row['Lineage'] == "European" and row['Does the bee have DWV?'] == "has DWV"):
            european_and_dwv = european_and_dwv + 1
        elif (row['Lineage'] == "European" and row['Does the bee have DWV?'] == "not infected with DWV"):
            european_and_no_dwv = european_and_no_dwv + 1
        elif (row['Lineage'] == "European" and row['Does the bee have DWV?'] == ""):
            european_and_no_data = european_and_no_data + 1
        elif (row['Lineage'] == "European" and row['Does the bee have DWV?'] == "no RNA "):
            european_and_no_rna = european_and_no_rna + 1   
            
        elif (row['Lineage'] == "no data" and row['Does the bee have DWV?'] == "has DWV"):
            no_data_and_dwv = no_data_and_dwv + 1
        elif (row['Lineage'] == "no data" and row['Does the bee have DWV?'] == "not infected with DWV"):
            no_data_and_no_dwv = no_data_and_no_dwv + 1
        elif (row['Lineage'] == "no data" and row['Does the bee have DWV?'] == ""):
            no_data_and_no_data = no_data_and_no_data + 1
        elif (row['Lineage'] == "no data" and row['Does the bee have DWV?'] == "no RNA "):
            no_data_and_no_rna = no_data_and_no_rna + 1 
                
        elif (row['Lineage'] == "other" and row['Does the bee have DWV?'] == "has DWV"):
            other_and_dwv = other_and_dwv + 1     
        elif (row['Lineage'] == "other" and row['Does the bee have DWV?'] == "not infected with DWV"):
            other_and_no_dwv = other_and_no_dwv + 1     
        elif (row['Lineage'] == "other" and row['Does the bee have DWV?'] == ""):
            other_and_no_data = other_and_no_data + 1 
        elif (row['Lineage'] == "other" and row['Does the bee have DWV?'] == "no RNA "):
            other_and_no_rna = other_and_no_rna + 1 
    
        
        
        
    print("Total entries: ", african_and_dwv + african_and_no_dwv + african_and_no_data + european_and_dwv + european_and_no_dwv + european_and_no_data + no_data_and_dwv + no_data_and_no_dwv + no_data_and_no_data
        + african_and_no_rna + european_and_no_rna + no_data_and_no_rna + other_and_dwv + other_and_no_dwv + other_and_no_data)
    print("\n")

    print("Total African bees: ", african)
    print("Total European bees: ", european)
    print("Total bees with no lineage data: ", no_data)
    print("Total bees with other lineage: ", other)
    print("\n")
    
    print("Total bees with DWV: ", has_dwv)
    print("Total bees with no DWV: ", has_no_dwv)
    print("Total bees with no DWV data: ", no_dwv_data)
    print("Total bees with no RNA: ", no_rna)
    print("\n")


    print("African bees with DWV: ", african_and_dwv)
    print("African bees with no DWV: ", african_and_no_dwv)
    print("African bees with no RNA: ", african_and_no_rna)
    print("African bees with no data: ", african_and_no_data )
    print("\n")


    print("European bees with DWV: ", european_and_dwv)
    print("European bees with no DWV: ", european_and_no_dwv)
    print("European bees with no RNA: ", european_and_no_rna)
    print("European bees with no data: ", european_and_no_data)
    print("\n")


    print("Other Lineage bees with DWV: ", other_and_dwv)
    print("Other Lineage bees with no DWV: ", other_and_no_dwv)
    print("Other Lineage bees with no RNA: ", other_and_no_rna)
    print("Other Lineage bees with no data: ", other_and_no_data)
    print("\n")

    
    print("No lineage data bees with DWV: ", no_data_and_dwv)
    print("No lineage data bees with no DWV: ", no_data_and_no_dwv)
    print("No lineage data bees with no RNA: ", no_data_and_no_rna)
    print("No lineage data bees with no data: ", no_data_and_no_data)