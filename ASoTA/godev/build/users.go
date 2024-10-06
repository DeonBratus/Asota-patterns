package main

// for all user interface
type User interface {
	GetName() string
	GetRole() usertype
	Work() string
}

//Trading agent
type TradingAgent struct {
	name string
	role usertype
}

func (ta *TradingAgent) GetName() string {
	return ta.name
}

func (ta *TradingAgent) GetRole() usertype {
	return ta.role
}

func (ta *TradingAgent) Work() string {
	return "is selling products"
}

func (ta *TradingAgent) CreateOrder() string {
	return "ORDER IS CREATED"
}

//Storage mananger
type StorageManager struct {
	name string
	role usertype
}

func (sm *StorageManager) GetName() string {
	return sm.name
}

func (sm *StorageManager) GetRole() usertype {
	return sm.role
}

func (sm *StorageManager) Work() string {
	return "Is work on storage"
}

//Shop owner
type ShopOwner struct {
	name string
	role usertype
}

func (so *ShopOwner) GetName() string {
	return so.name
}

func (so *ShopOwner) GetRole() usertype {
	return so.role
}

func (so ShopOwner) Work() string {
	return "Check pribil'"
}

type usertype int

const (
	TradingAgentType usertype = iota
	StorageManagerType
	ShopOwnerType
)

// Factory Method. In here create object which based on choosed classes of user
func CreateUser(userType usertype, username string) User {
	switch userType {
	case TradingAgentType:
		return &TradingAgent{name: username, role: TradingAgentType}
	case StorageManagerType:
		return &StorageManager{name: username, role: StorageManagerType}
	case ShopOwnerType:
		return &ShopOwner{name: username, role: ShopOwnerType}
	default:
		return nil
	}
}
