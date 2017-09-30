package main

import (
	"fmt"
	"net/http"
	"strings"
)

func homeHandler(w http.ResponseWriter, r *http.Request) {
	urlPath := r.URL.Path[1:]
	parts := strings.Split(urlPath, "/")
	fmt.Fprintln(w, parts)
}

func main() {
	http.HandleFunc("/home/", homeHandler)
	http.HandleFunc("/store/", homeHandler)
	fmt.Println("Starting server ...")
	http.ListenAndServe(":3001", nil)
}
