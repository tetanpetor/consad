def groupedSimilarFilenames(filenames):
    # Sort filenames to ensure similar ones are grouped together
    filenames.sort()
    
    groups = []
    current_group = []
    
    for filename in filenames:
        if current_group and not filename.startswith(current_group[0][0]):
            groups.append(current_group)
            current_group = []
        current_group.append(filename)
    
    if current_group:
        groups.append(current_group)
    
    return groups
