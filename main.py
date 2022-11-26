import pandas as pd
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import FOAF, XSD, RDFS, SH

url = 'http://raw.githubusercontent.com/javierdiazparada/csv_rdf/main/Games.csv'
df = pd.read_csv(url, sep=",", quotechar='"')

name = URIRef('name')
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
    g.add((URIRef(ex+givenName), RDF.type, URIRef(schema+videoGame)))
    g.add((URIRef(ex+givenName), URIRef(schema+name), Literal(row['Name'], datatype=XSD.string)))
    g.add((URIRef(ex+givenName), URIRef(schema+genre), Literal(row['Genre'], datatype=XSD.string)))
    g.add((URIRef(ex+givenName), URIRef(schema+videoGameSeries), Literal(row['Series'], datatype=XSD.string)))
    g.add((URIRef(ex+givenName), URIRef(schema+releaseDate), Literal(row['Release'], datatype=XSD.gMonthDay)))
    g.add((URIRef(ex+givenName), URIRef(useful+developer), Literal(row['Developer'], datatype=XSD.string)))
    g.add((URIRef(ex+givenName), URIRef(purl+publisher), Literal(row['Publisher'], datatype=XSD.string)))

with open("RDF_Games.txt",'x', encoding="utf-8") as f:
    text = g.serialize(format='turtle').encode('UTF-8').decode()
    f.write(text)