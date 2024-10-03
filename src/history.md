 1894  ls
 1895  vim .bashrc 
 1896  vim .bash_aliases
 1897  cat .bash_aliases 
 1898  vim .bashrc 
 1899  cat .bashrc 
 1900  exit
 1901  /bin/python3 /home/rickymal/.vscode/extensions/ms-python.python-2024.14.1-linux-x64/python_files/printEnvVariablesToFile.py /home/rickymal/.vscode/extensions/ms-python.python-2024.14.1-linux-x64/python_files/deactivate/bash/envVars.txt
 1902  parser
 1903  clear
 1904  cd Área\ de\ trabalho/
 1905  cd aurora-lang/
 1906  clear
 1907  history
 1908  alias
 1909  clear
 1910  alias
 1911  parser lunaLexer.g4
 1912  clear
 1913  parser
 1914  parser -lib . -o spec
 1915  cd src/
 1916  parser -lib . -o spec
 1917  parser -lib . -o spec/
 1918  clear
 1919  alias
 1920  parser lunaLexer.g4 
 1921  parser luna.g4 
 1922  javac luna*.java
 1923  grun --help
 1924  grun ship-calculus/basic.luna 
 1925  grun -tree ship-calculus/basic.luna 
 1926  grun -tokens ship-calculus/basic.luna 
 1927  grun -gui ship-calculus/basic.luna 
 1928  grun luna -gui ship-calculus/basic.luna 
 1929  ls -la
 1930  grun luna sourceFile -gui ship-calculus/basic.luna 
 1931  javac *.java
 1932  grun luna sourceFile -gui ship-calculus/basic.luna 
 1933  clear
 1934  alias
 1935  java -Xmx500M -cp "/usr/local/lib/antlr-4.9.3-complete.jar" org.antlr.v4.Tool lunaLexer.g4 
 1936  java -Xmx500M -cp "/usr/local/lib/antlr-4.9.3-complete.jar" org.antlr.v4.Tool -visitor luna.g4 
 1937  grun luna sourceFile -tree ship-calculus/basic.luna 
 1938  clear
 1939  parser Hello.g4 
 1940  grun Hello -r -tree
 1941  javac Hello*.java
 1942  grun Hello r -tree
 1943  alias
 1944  clear
 1945  java -jar /usr/local/lib/antlr-4.9.3-complete.jar lunaLexer.g4
 1946  java -jar /usr/local/lib/antlr-4.9.3-complete.jar luna.g4 
 1947  javac -cp .:/usr/local/lib/antlr-4.9.3-complete.jar *.java
 1948  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar org.antlr.v4.gui.TestRig luna sourceFile -tree ship-calculus/basic.luna 
 1949  c
 1950  clear
 1951  ls *.java
 1952  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar org.antlr.v4.gui.TestRig luna sourceFile -tree ship-calculus/basic.luna 
 1953  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar org.antlr.v4.gui.TestRig luna program -tree ship-calculus/basic.luna 
 1954  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar org.antlr.v4.gui.TestRig luna xmlBlock -tree ship-calculus/basic.luna 
 1955  clear
 1956  parser luna.g4 
 1957  clear
 1958  alias
 1959  java -cp /usr/local/lib/antlr-4.9.3-complete.jar luna.g4
 1960  history
 1961  clear
 1962  java -jar /usr/local/lib/antlr-4.9.3-complete.jar -visitor lunau
 1963  java -jar /usr/local/lib/antlr-4.9.3-complete.jar -visitor luna.g4
 1964  java -jar /usr/local/lib/antlr-4.9.3-complete.jar -visitor lunaParser.g4 
 1965  java -jar /usr/local/lib/antlr-4.9.3-complete.jar -visitor lunaLexer.g4 
 1966  java -jar /usr/local/lib/antlr-4.9.3-complete.jar -visitor lunaParser.g4 
 1967  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar org.antlr.v4.gui.TestRig luna sourceFile -tokens ship-calculus/basic.luna 
 1968  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar org.antlr.v4.gui.TestRig lunaParser sourceFile -tokens ship-calculus/basic.luna 
 1969  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar org.antlr.v4.gui.TestRig lunaParse sourceFile -tokens ship-calculus/basic.luna 
 1970  java -cp ".:/usr/local/lib/antlr-4.9.3-complete.jar" org.antlr.v4.gui.TestRig lunaParse sourceFile -tokens ship-calculus/basic.luna 
 1971  java -cp /usr/local/lib/antlr-4.9.3-complete.jar org.antlr.v4.gui.TestRig lunaParse sourceFile -tokens ship-calculus/basic.luna 
 1972  java -cp .  org.antlr.v4.gui.TestRig lunaParse sourceFile -tokens ship-calculus/basic.luna 
 1973  java -cp /usr/local/lib/antlr-4.9.3-complete.jar org.antlr.v4.gui.TestRig lunaParse sourceFile -tokens ship-calculus/basic.luna 
 1974  java -cp /usr/local/lib/antlr-4.9.3-complete.jar org.antlr.v4.gui.TestRig lunaParfdfdsfsse sourceFile -tokens ship-calculus/basic.luna 
 1975  java -jar /usr/local/lib/antlr-4.9.3-complete.jar -o /dist lunaLexer.g4 
 1976  java -jar /usr/local/lib/antlr-4.9.3-complete.jar -o dist lunaLexer.g4 
 1977  java -jar /usr/local/lib/antlr-4.9.3-complete.jar -o dist lunaParser.g4 
 1978  java -jar ./dist/lunaParser.java
 1979  java -cp ./dist/lunaParser.java
 1980  java -cp ./dist/lunaParser.java -tree
 1981  java -cp "./dist/lunaParser.java -tree"
 1982  clear
 1983  parser lunaParser.g4 
 1984  javac *.java
 1985  clear
 1986  parser -visitor lunaParser.g4 
 1987  parser -visitor -o /dist lunaParser.g4 
 1988  parser -visitor -o /dist lunaLexer.g4 
 1989  parser
 1990  parser lunaLexer.g4 
 1991  parser -visitor -o /dist lunaParser.g4 
 1992  j
 1993  alias
 1994  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar 
 1995  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar -o dist lunaParser.g4 
 1996  java -jar .:/usr/local/lib/antlr-4.9.3-complete.jar -o dist lunaParser.g4 
 1997  exit
 1998  sudo java -jar antlrworks-1.5.2-complete.jar 
 1999  clear
 2000  code .
 2001  clear
 2002  alias
 2003  parser --helpo
 2004  parser --help
 2005  parser --h
 2006  parser -g
 2007  parser -h
 2008  parsere
 2009  parser
 2010  cd sr
 2011  cd src/
 2012  parser lunaLexer.g4 
 2013  parser lunaParser.g4 
 2014  ls
 2015  ls -la
 2016  java -jar lunaParser.java
 2017  java -cp . lunaParser.java
 2018  clear
 2019  alias
 2020  javac lunaParser*.java
 2021  javac luna*.java
 2022  clear
 2023  parser lunaParser.g4 
 2024  javac luna*.java
 2025  grun lunaParser sourceFile -tree
 2026  grun luna sourceFile -tree
 2027  clear
 2028  grun luna sourceFile -gui ship-calculus/basic.luna 
 2029  clear
 2030  grun luna sourceFile -gui ship-calculus/basic.luna 
 2031  grun luna sourceFile -gui ship-calculus/main.go 
 2032  parser lunaParser
 2033  parser lunaParser.g4 
 2034  clear
 2035  parser lunaParser.g4 
 2036  clear
 2037  parser lunaParser.g4 
 2038  clear
 2039  parser lunaParser.g4 
 2040  clear
 2041  parser lunaParser.g4 
 2042  javac luna*.java
 2043  clear
 2044  parser lunaParser.g4 
 2045  clear
 2046  javac luna*.java
 2047  javac luna*.javaclear
 2048  clear
 2049  javac -cp .:java luna*.java
 2050  javac -cp .:java/luna*.java
 2051  javac -cp .:java/ luna*.java
 2052  clear
 2053  javac -cp .:java/ luna*.java
 2054  javac luna*.java
 2055  clear
 2056  parser lunaParser.g4 
 2057  parser lunaLexer.g4 
 2058  clear
 2059  parser lunaLexer.g4 
 2060  javac luna*.java
 2061  clear
 2062  javac -cp .:/usr/local/lib/antlr-4.9.3-complete.jar:java/ luna*.java
 2063  clear
 2064  javac -cp .:/usr/local/lib/antlr-4.9.3-complete.jar:java/ luna*.java
 2065  grun luna sourceFile -gui ship-calculus/main.go 
 2066  clear
 2067  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar:java/ org.antlr.v4.gui.TestRig luna sourceFile -tree 
 2068  cler
 2069  clear
 2070  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar:java/ org.antlr.v4.gui.TestRig luna sourceFile -tree ship-calculus/main.go 
 2071  history
rickymal@rickymal-550XDA:~/Área de trabalho/aurora-lang/src$ 



 1954  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar org.antlr.v4.gui.TestRig luna xmlBlock -tree ship-calculus/basic.luna 
 1955  clear
 1956  parser luna.g4 
 1957  clear
 1958  alias
 1959  java -cp /usr/local/lib/antlr-4.9.3-complete.jar luna.g4
 1960  history
 1961  clear
 1962  java -jar /usr/local/lib/antlr-4.9.3-complete.jar -visitor lunau
 1963  java -jar /usr/local/lib/antlr-4.9.3-complete.jar -visitor luna.g4
 1964  java -jar /usr/local/lib/antlr-4.9.3-complete.jar -visitor lunaParser.g4 
 1965  java -jar /usr/local/lib/antlr-4.9.3-complete.jar -visitor lunaLexer.g4 
 1966  java -jar /usr/local/lib/antlr-4.9.3-complete.jar -visitor lunaParser.g4 
 1967  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar org.antlr.v4.gui.TestRig luna sourceFile -tokens ship-calculus/basic.luna 
 1968  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar org.antlr.v4.gui.TestRig lunaParser sourceFile -tokens ship-calculus/basic.luna 
 1969  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar org.antlr.v4.gui.TestRig lunaParse sourceFile -tokens ship-calculus/basic.luna 
 1970  java -cp ".:/usr/local/lib/antlr-4.9.3-complete.jar" org.antlr.v4.gui.TestRig lunaParse sourceFile -tokens ship-calculus/basic.luna 
 1971  java -cp /usr/local/lib/antlr-4.9.3-complete.jar org.antlr.v4.gui.TestRig lunaParse sourceFile -tokens ship-calculus/basic.luna 
 1972  java -cp .  org.antlr.v4.gui.TestRig lunaParse sourceFile -tokens ship-calculus/basic.luna 
 1973  java -cp /usr/local/lib/antlr-4.9.3-complete.jar org.antlr.v4.gui.TestRig lunaParse sourceFile -tokens ship-calculus/basic.luna 
 1974  java -cp /usr/local/lib/antlr-4.9.3-complete.jar org.antlr.v4.gui.TestRig lunaParfdfdsfsse sourceFile -tokens ship-calculus/basic.luna 
 1975  java -jar /usr/local/lib/antlr-4.9.3-complete.jar -o /dist lunaLexer.g4 
 1976  java -jar /usr/local/lib/antlr-4.9.3-complete.jar -o dist lunaLexer.g4 
 1977  java -jar /usr/local/lib/antlr-4.9.3-complete.jar -o dist lunaParser.g4 
 1978  java -jar ./dist/lunaParser.java
 1979  java -cp ./dist/lunaParser.java
 1980  java -cp ./dist/lunaParser.java -tree
 1981  java -cp "./dist/lunaParser.java -tree"
 1982  clear
 1983  parser lunaParser.g4 
 1984  javac *.java
 1985  clear
 1986  parser -visitor lunaParser.g4 
 1987  parser -visitor -o /dist lunaParser.g4 
 1988  parser -visitor -o /dist lunaLexer.g4 
 1989  parser
 1990  parser lunaLexer.g4 
 1991  parser -visitor -o /dist lunaParser.g4 
 1992  j
 1993  alias
 1994  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar 
 1995  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar -o dist lunaParser.g4 
 1996  java -jar .:/usr/local/lib/antlr-4.9.3-complete.jar -o dist lunaParser.g4 
 1997  exit
 1998  sudo java -jar antlrworks-1.5.2-complete.jar 
 1999  clear
 2000  code .
 2001  clear
 2002  alias
 2003  parser --helpo
 2004  parser --help
 2005  parser --h
 2006  parser -g
 2007  parser -h
 2008  parsere
 2009  parser
 2010  cd sr
 2011  cd src/
 2012  parser lunaLexer.g4 
 2013  parser lunaParser.g4 
 2014  ls
 2015  ls -la
 2016  java -jar lunaParser.java
 2017  java -cp . lunaParser.java
 2018  clear
 2019  alias
 2020  javac lunaParser*.java
 2021  javac luna*.java
 2022  clear
 2023  parser lunaParser.g4 
 2024  javac luna*.java
 2025  grun lunaParser sourceFile -tree
 2026  grun luna sourceFile -tree
 2027  clear
 2028  grun luna sourceFile -gui ship-calculus/basic.luna 
 2029  clear
 2030  grun luna sourceFile -gui ship-calculus/basic.luna 
 2031  grun luna sourceFile -gui ship-calculus/main.go 
 2032  parser lunaParser
 2033  parser lunaParser.g4 
 2034  clear
 2035  parser lunaParser.g4 
 2036  clear
 2037  parser lunaParser.g4 
 2038  clear
 2039  parser lunaParser.g4 
 2040  clear
 2041  parser lunaParser.g4 
 2042  javac luna*.java
 2043  clear
 2044  parser lunaParser.g4 
 2045  clear
 2046  javac luna*.java
 2047  javac luna*.javaclear
 2048  clear
 2049  javac -cp .:java luna*.java
 2050  javac -cp .:java/luna*.java
 2051  javac -cp .:java/ luna*.java
 2052  clear
 2053  javac -cp .:java/ luna*.java
 2054  javac luna*.java
 2055  clear
 2056  parser lunaParser.g4 
 2057  parser lunaLexer.g4 
 2058  clear
 2059  parser lunaLexer.g4 
 2060  javac luna*.java
 2061  clear
 2062  javac -cp .:/usr/local/lib/antlr-4.9.3-complete.jar:java/ luna*.java
 2063  clear
 2064  javac -cp .:/usr/local/lib/antlr-4.9.3-complete.jar:java/ luna*.java
 2065  grun luna sourceFile -gui ship-calculus/main.go 
 2066  clear
 2067  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar:java/ org.antlr.v4.gui.TestRig luna sourceFile -tree 
 2068  cler
 2069  clear
 2070  java -cp .:/usr/local/lib/antlr-4.9.3-complete.jar:java/ org.antlr.v4.gui.TestRig luna sourceFile -tree ship-calculus/main.go 
 2071  history
 2072  clear
 2073  parser lunaLexer.g4 lunaParser.g4 
 2074  parser lunaLexer.g4
 2075  clear
 2076  parser lunaLexer.g4
 2077  parser lunaParser.g4 
 2078  clear
 2079  parser lunaParser.g4 
 2080  clear
 2081  javac luna*.java
 2082  clear
 2083  grun luna sourceFile -tree ship-calculus/main.go 
 2084  grun luna sourceFile -gui ship-calculus/main.go 
 2085  grun luna sourceFile -tree ship-calculus/computation.luna 
 2086  clear
 2087  grun luna sourceFile -tree ship-calculus/computation.luna 
 2088  clear
 2089  parser lunaLexer.
 2090  parser lunaLexer.g4 
 2091  parser lunaParser.g4 
 2092  clear
 2093  javac luna*.java
 2094  grun luna sourceFile -tree ship-calculus/computation.luna 
 2095  grun luna sourceFile -tree ship-calculus/main.go 
 2096  grun luna sourceFile -tree ship-calculus/computation.luna 
 2097  history
rickymal@rickymal-550XDA:~/Área de trabalho/aurora-lang/src$ 


