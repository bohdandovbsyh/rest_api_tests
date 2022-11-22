import xml.etree.ElementTree as ET


# tree = ET.parse('movies.xml')
# root = tree.getroot()


# print(root.tag)

# for child in root:
#     print(child.tag, child.attrib)
# print('\n')
# # print([elem.tag for elem in root.iter()])
# print(ET.tostring(root, encoding='utf8').decode('utf8'))

# for movie in root.iter('movie'):
#     # print(movie.attrib)
#     for child in movie:
#         print(f"{child.tag} : {child.text}")

# for description in root.iter('description'):
#     print(description.text)

# for movie in root.findall("./genre/decade/movie/[rating='PG-13']"):
#     print(movie.attrib)

# for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
#     print(movie.attrib)

# for movie in root.findall(".//format[@multiple='Yes']..."):
#     print(movie.attrib)

# karate_kid = root.find(".//movie[@title='karate_kid 2']")
# karate_kid.attrib["title"] = "2 THE KARATE KID"
# batman = root.find(".//movie[@title='Batman Returns']")
# batman.attrib['title'] = 'Batman Returns 2'
# tree.write("movies.xml")

# import re
#
# for form in root.findall("./genre/decade/movie/format"):
#     print(form.attrib, form.text)
#
# print('*****************************************************')
#
# for form in root.findall("./genre/decade/movie/format"):
#     # Search for the commas in the format text
#     match = re.search(',', form.text)
#     if match:
#         form.set('multiple', 'Yes')
#     else:
#         form.set('multiple', 'No')
#
# # Write out the tree to the file again
# tree.write("movies.xml")
#
# tree = ET.parse('movies.xml')
# root = tree.getroot()
#
# for form in root.findall("./genre/decade/movie/format"):
#     print(form.attrib, form.text)

class Movie:
    def __init__(self, title: str, format: str, year: int, rating: str, description: str):
        self.title = title
        self.format = format
        self.year = year
        self.rating = rating
        self.description = description

    @classmethod
    def from_xml(cls, path: str):
        tree = ET.parse(path)
        root = tree.getroot()
        movies = []
        for movie in root.iter('movie'):
            data = {'title': movie.attrib['title']}
            for child in movie:
                data[child.tag] = child.text
            movies.append(cls(**data))
        return movies

    def __str__(self):
        data = ""
        for key, value in self.__dict__.items():
            data += f"\t{key} : {value}\n"
        return data


movies = Movie.from_xml('movies.xml')

print(movies[0].description)

for m in movies:
    print(m)
