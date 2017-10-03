package main

import (
	"fmt"
	"net/http"
	"os"
	"strings"
)

var store = make(map[string]string)
var SECRET = os.Getenv("SECRET")

func homeHandler(w http.ResponseWriter, r *http.Request) {
	urlPath := r.URL.Path[1:]
	parts := strings.Split(urlPath, "/")
	fmt.Fprintln(w, parts)
}

func storeHandler(w http.ResponseWriter, r *http.Request) {
	urlPath := r.URL.Path[1:]
	fmt.Println(urlPath)
	parts := strings.Split(urlPath, "/")

	if len(SECRET) == 0 || len(parts) != 3 {
		http.NotFound(w, r)
		return
	}
	secret, key, value := parts[0], parts[1], parts[2]
	if key == "get" {
		fmt.Fprintln(w, store)
		return
	}

	if secret != "111" {
		http.NotFound(w, r)
		return
	}
	store[key] = value
	fmt.Fprintln(w, store, len(parts))
}

func main() {
	// http.HandleFunc("/home/", homeHandler)
	http.HandleFunc(fmt.Sprintf("/%s/", SECRET), storeHandler)
	fmt.Println("Starting server ...")
	http.ListenAndServe(":3001", nil)
}
