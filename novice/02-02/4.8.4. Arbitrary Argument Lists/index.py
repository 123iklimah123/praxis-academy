def write_multiple_items(file, separator, *args):
     file.write(separator.join(args))

def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")   

concat("earth", "mars", "venus", sep=".")