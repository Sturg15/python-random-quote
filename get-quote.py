def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  #print(quotes[1], end = '')
  #print(quotes[0]) This will print with no spaces
  for i in range(0, len(quotes)):
    print(quotes[i])


if __name__== "__main__":
  primary()
