# must be run from within the logistic regression folder
# example: fish logisticRegression.fish data/logisticData.csv

if test (count $argv) -ne 1
    echo 'Please provide a data file'
    exit 1
end

javac -cp ".:lib/*" src/*.java -d .
java -cp ".:lib/*" GradientDescent $argv[1]
set files *.class
rm $files