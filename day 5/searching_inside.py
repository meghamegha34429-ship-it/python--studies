def search(flights, source, dest):
    for f in flights:
        if flights[f]["source"] == source and flights[f]["dest"] == dest:
            return f
