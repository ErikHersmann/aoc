library(readr); library(stringi)
data <- read_file("day0_input.txt")
hm <- stri_split_lines1(data)
c = 0; arr0 = c()
for(i in 1:length(hm)){
  if(hm[i]!=""){
    c = c + as.numeric(hm[i])
  } else {
    arr0 = append(arr0, c); c = 0
  }
}
arr0 <- sort(arr0)
arr0[length(arr0)]; arr0[length(arr0)]+ arr0[length(arr0)-1]+ arr0[length(arr0)-2]
