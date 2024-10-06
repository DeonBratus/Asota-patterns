package main

import (
	"fmt"
)

func main() {
	user := CreateUser(TradingAgentType, "Abdul")
	fmt.Printf("%v with name %s %s now\n", user.GetRole(), user.GetName(), user.Work())

	if tradUser, ok := user.(*TradingAgent); ok {
		fmt.Print(tradUser.name, ": ", tradUser.CreateOrder())
	}

}
