library(reticulate)

#manipulation sur R
mpgData <- mtcars
#conserver le nom de rang
liste=as.list(mpgData)
#conserver le nom de colum
list_l <- as.list(as.data.frame(t(mpgData)))
write(liste, file = "data",sep = ",")

#manipulation avec un fichier de python
source_python("/Users/xinyue/shiny/algo.py")
Data <- range_csv("/Users/xinyue/shiny/test_dataframe.csv")
summary(Data)


