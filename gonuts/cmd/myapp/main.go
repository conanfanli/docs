package main

import (
	"fmt"
	"net/http"
	"path"
)

func handler(w http.ResponseWriter, r *http.Request) {
	first, text := path.Split(r.URL.Path[1:])
	fmt.Fprintln(w, first, text)
}

func main() {
	http.HandleFunc("/", handler)
	fmt.Println("Starting server ...")
	http.ListenAndServe(":3000", nil)
}
