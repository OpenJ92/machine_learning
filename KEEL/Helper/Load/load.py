import pandas as pd
import numpy as np
import re

class Base_Load:
    def __init__(self, dir_, datafile, headerfile):
        self.dir = dir_
        self.datafile = datafile
        self.headerfile = headerfile
        self.inputs, self.attributes = self.read_inputs(), self.read_attributes()
        self.data = self.construct_data()

    def data(self):
        return pd.read_csv(f"{self.dir}/{self.datafile}", sep='\s*,\s*', engine='python')

    def describe(self):
        return self.data().describe()

    def header_file(self):
        return f"{self.dir}/{self.headerfile}"

    def read_attributes(self):
        pattern = r'\@attribute.*\n'
        text = open(self.header_file(), "r").read()
        pt = re.findall(pattern, text)
        pt = [i.replace("@attributes", "").replace("\n", "").split(' ') for i in pt]
        return pt

    def read_inputs(self):
        pattern = r'\@inputs.*\n'
        text = open(self.header_file(), "r").read()
        pt = re.search(pattern, text)[0]
        pt = pt.replace("@inputs", "").replace("\n", "").split(' ')
        pt = [i.replace(" ", "").replace(",", "") for i in pt]
        return pt[1:]

    def attribute_dictionary(self):
        dictionary = {}
        for attribute in self.attributes:
            dictionary[attribute[1]] = {"name":attribute[1], "abstraction":attribute[2], "selector":attribute[3], "bounds":attribute[4]}
        return dictionary

    def replace_object_columns(self, data):
        for col in data.columns:
            if data[col].dtype == np.object:
                unique_obj = data[col].unique()
                data[col] = data[col].replace(unique_obj, list(range(len(unique_obj))))
        return data

    def construct_data(self):
        data = self.data()
        return self.replace_object_columns(data)

