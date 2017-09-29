package main

import (
	"fmt"
	"net/http"
	"strings"
)

func handler(w http.ResponseWriter, request *http.Request) {
	urlPath := request.URL.Path[1:]

	fmt.Fprintln(w, strings.Split(urlPath, "/"))
}

func main() {
	http.HandleFunc("/", handler)
	fmt.Println("Starting server ...")
	http.ListenAndServe(":3000", nil)
}
