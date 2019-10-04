from datetime import datetime
import abc


class WriteFile:

    __metaclass__ = abc.ABCMeta

    def __init__(self, file_name):
        self.file_name = file_name

    def write_line(self, text):
        fh = open(self.file_name, 'a')
        fh.write(text + '\n')
        fh.close()

    @abc.abstractmethod
    def write(self):
        return


class CsvFile(WriteFile):

    def __init__(self, filename, delimiter):
        super(CsvFile, self).__init__(filename)
        self.delimiter = delimiter

    def write(self, this_list):
        line = self.delimiter.join(this_list)
        self.write_line(line)


class LogFile(WriteFile):

    def write(self, this_line):
        dt = datetime.now()
        date_string = dt.strftime('%Y-%m-%d %H:%M')
        self.write_line('{0}   {1}'.format(date_string, this_line))






