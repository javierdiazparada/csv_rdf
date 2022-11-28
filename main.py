import pandas as pd
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import FOAF, XSD, RDFS, SH

url = 'http://raw.githubusercontent.com/javierdiazparada/csv_rdf/main/Games.csv'
df = pd.read_csv(url, sep=",", quotechar='"')

name = URIRef('name')
sales = URIRef('sales')
director = URIRef('director')
genre = URIRef('genre')
videoGame = URIRef('VideoGame')
videoGameSeries = URIRef('VideoGameSeries')
releaseDate = URIRef('releaseDate')
developer = URIRef('doap#developer')
publisher = URIRef('publisher')

g = Graph()
ex = Namespace('http://example.org/')
schema = Namespace('http://schema.org/')
useful = Namespace('http://usefulinc.com/ns/')
purl = Namespace('http://purl.org/dc/elements/1.1/')

def date_default(dold):
    if dold[0] == 'Jan':
        if int(dold[1]) <= 22:
            dnew = str(int(dold[1])+2000) + '-01'
            return dnew
        else:
            dnew = str(int(dold[1])+1900) + '-01'
            return dnew
    elif dold[0] == 'Feb':
        if int(dold[1]) <= 22:
            dnew = str(int(dold[1]) + 2000) + '-02'
            return dnew
        else:
            dnew = str(int(dold[1]) + 1900) + '-02'
            return dnew
    elif dold[0] == 'Mar':
        if int(dold[1]) <= 22:
            dnew = str(int(dold[1]) + 2000) + '-03'
            return dnew
        else:
            dnew = str(int(dold[1]) + 1900) + '-03'
            return dnew
    elif dold[0] == 'Apr':
        if int(dold[1]) <= 22:
            dnew = str(int(dold[1]) + 2000) + '-04'
            return dnew
        else:
            dnew = str(int(dold[1]) + 1900) + '-04'
            return dnew
    elif dold[0] == 'May':
        if int(dold[1]) <= 22:
            dnew = str(int(dold[1]) + 2000) + '-05'
            return dnew
        else:
            dnew = str(int(dold[1]) + 1900) + '-05'
            return dnew
    elif dold[0] == 'Jun':
        if int(dold[1]) <= 22:
            dnew = str(int(dold[1]) + 2000) + '-06'
            return dnew
        else:
            dnew = str(int(dold[1]) + 1900) + '-06'
            return dnew
    elif dold[0] == 'Jul':
        if int(dold[1]) <= 22:
            dnew = str(int(dold[1]) + 2000) + '-07'
            return dnew
        else:
            dnew = str(int(dold[1]) + 1900) + '-07'
            return dnew
    elif dold[0] == 'Aug':
        if int(dold[1]) <= 22:
            dnew = str(int(dold[1]) + 2000) + '-08'
            return dnew
        else:
            dnew = str(int(dold[1]) + 1900) + '-08'
            return dnew
    elif dold[0] == 'Sep':
        if int(dold[1]) <= 22:
            dnew = str(int(dold[1]) + 2000) + '-09'
            return dnew
        else:
            dnew = str(int(dold[1]) + 1900) + '-09'
            return dnew
    elif dold[0] == 'Oct':
        if int(dold[1]) <= 22:
            dnew = str(int(dold[1]) + 2000) + '-10'
            return dnew
        else:
            dnew = str(int(dold[1]) + 1900) + '-10'
            return dnew
    elif dold[0] == 'Nov':
        if int(dold[1]) <= 22:
            dnew = str(int(dold[1]) + 2000) + '-11'
            return dnew
        else:
            dnew = str(int(dold[1]) + 1900) + '-11'
            return dnew
    elif dold[0] == 'Dec':
        if int(dold[1]) <= 22:
            dnew = str(int(dold[1]) + 2000) + '-12'
            return dnew
        else:
            dnew = str(int(dold[1]) + 1900) + '-12'
            return dnew


def name_default(sold):
    snew = sold
    snew = snew.replace("'", '')
    snew = snew.replace(' ', '')
    snew = snew.replace(':', '')
    snew = snew.replace(".", '')
    snew = snew.replace(',', '')
    snew = snew.replace('?', '')
    snew = snew.replace("/", '')
    snew = snew.replace('&', '')
    snew = snew.replace('$', '')
    return snew


for index, row in df.iterrows():

    givenName = name_default(row['Name'])
    g.add((URIRef(ex + givenName), RDF.type, URIRef(schema + videoGame)))
    g.add((URIRef(ex + givenName), URIRef(schema + name), Literal(row['Name'], datatype=XSD.string)))
    g.add((URIRef(ex + givenName), URIRef(ex + sales), Literal(row['Sales'] * 1000000.0, datatype=XSD.float)))
    Genres = row['Genre'].split(',\xa0')
    for i in Genres:
        j = i.capitalize()
        g.add((URIRef(ex + givenName), URIRef(schema + genre), Literal(j)))

    g.add((URIRef(ex + givenName), URIRef(schema + videoGameSeries), Literal(row['Series'])))

    Date = date_default(row['Release'].split('-'))

    g.add((URIRef(ex + givenName), URIRef(schema + releaseDate), Literal(Date, datatype=XSD.gYearMonth)))
    g.add((URIRef(ex + givenName), URIRef(useful + developer), Literal(row['Developer'])))
    g.add((URIRef(ex + givenName), URIRef(purl + publisher), Literal(row['Publisher'])))

with open("RDF_Games.txt", 'x', encoding="utf-8") as f:
    text = g.serialize(format='turtle').encode('UTF-8').decode()
    f.write(text)
