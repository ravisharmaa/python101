from solution import WriteFile, CsvFormatter, LogFormatter

write_to_csv = WriteFile('text2.csv', CsvFormatter())
write_to_log = WriteFile('log.txt', LogFormatter())

write_to_csv.write(['a','b,2','c','d'])
write_to_csv.write('this is another log message')

write_to_csv.close()
write_to_log.close()
