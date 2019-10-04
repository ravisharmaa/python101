from datetime import datetime


class WriteFile:

    def __init__(self, file_name, writer):
        self.fh = open(file_name, 'w')
        self.formatter = writer

    def write(self, text):
        self.fh.write(self.formatter.format(text))

    def close(self):
        self.fh.close()


class CsvFormatter:

    def __init__(self):
        self.delimiter = ','

    def format(self, this_list):
        new_list = []
        for element in this_list:
            if self.delimiter in this_list:
                new_list.append('"{0}"'.format(element))
            else:
                new_list.append(element)
        return self.delimiter.join(new_list)


class LogFormatter:

    def format(self, this_line):
        dt = datetime.now()
        date_str = dt.strftime('%Y-%m-%d %H:%M')
        return "{0}  {1}".format(date_str, this_line)
