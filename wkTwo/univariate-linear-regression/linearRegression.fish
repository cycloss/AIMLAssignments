
# example: fish linearRegression.fish data/testData.csv

if test (count $argv) -ne 1
    echo 'Please provide a data file'
    exit 1
end

javac -cp ".:lib/*" src/*.java -d .
java -cp ".:lib/*" GradientDescentNonLinear $argv[1]
set files *.class
rm $files