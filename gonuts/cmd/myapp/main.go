package main

import (
	"fmt"
	"net/http"
	"strings"
)

var store = make(map[string]string)

func homeHandler(w http.ResponseWriter, r *http.Request) {
	urlPath := r.URL.Path[1:]
	parts := strings.Split(urlPath, "/")
	fmt.Fprintln(w, parts)
}

func storeHandler(w http.ResponseWriter, r *http.Request) {
	urlPath := r.URL.Path[1:]
    parts := strings.Split(urlPath, "/")
    key, value := parts[1], parts[2]
    if key == "get" {
        fmt.Fprintln(w, store)
        return
    }
    store[key] = value
	fmt.Fprintln(w, store)
}

func main() {
	http.HandleFunc("/home/", homeHandler)
	http.HandleFunc("/store/", storeHandler)
	fmt.Println("Starting server ...")
	http.ListenAndServe(":3001", nil)
}
