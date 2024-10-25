

# Asota System Project

**Asota System** (Authomatization Sytem Of Trading Agents) — это система управления заказами и обработка платежей, которая использует роли пользователей, такие как *Торговый агент* и *Менеджер склада*. Пользователи взаимодействуют с системой через фасадный интерфейс (`AsotaFacade`), который предоставляет методы для добавления товаров на склад, создания заказов и обработки платежей. Поддерживаются различные типы платежей, включая СБП, банковскую карту и наличные.

## Структура проекта

- **asota.py**: Содержит класс `AsotaFacade`, который предоставляет единый интерфейс для управления пользователями и заказами.
- **users.py**: Определяет роли (`Roles`), доступные в системе, включая *Торгового агента* и *Менеджера склада*.
- **product.py**: Определяет класс `Product`, представляющий продукты и их цену.
- **payment.py**: Предоставляет классы для различных типов оплаты (`SBP_Payment`, `CreditCardPayment`, `CashPayment`), которые обрабатывают платежи в зависимости от выбранного метода.

## Инструкция по использованию

### Шаг 1: Инициализация системы Asota
Импортируйте необходимые классы, создайте экземпляр `AsotaFacade` и добавьте пользователя с заданной ролью.

```python
from asota import AsotaFacade
from users import Roles

asota = AsotaFacade()
user = asota.add_user_to_system(Roles.trading_agent, "Vanya")
asota.enter_to_system(user=user)
```

### Шаг 2: Управление складом
Если пользователь — **Менеджер склада**, он может создать список товаров и добавить их на склад.

```python
from product import Product

# Создаем список товаров с количеством
product_list_of_warehouse = [
    [Product("Otvertka", 1.2), 2],
    [Product("Shurik", 30.1), 4],
    [Product("Molotok", 2), 10]
]

# Добавляем товары на склад
asota.add_items_to_warehouse(product_list_of_warehouse)
```

### Шаг 3: Создание заказа (для Торгового агента)
Если пользователь — **Торговый агент**, он может создать заказ на основе товаров, доступных на складе. Метод `create_order` требует список товаров, информацию о клиенте, сумму от клиента, тип оплаты и соответствующие данные по оплате.

```python
from payment import SBP_Payment

# Определяем заказанные товары и количество
ordered_list = [
    [Product("Otvertka", 1.2), 2],
    [Product("Shurik", 30.1), 1]
]

# Создаем заказ с указанием типа оплаты и информации о клиенте
asota.create_order(
    product_list=ordered_list,
    customer_name="Bomj",
    amount_from_cust=200,
    payment_type=SBP_Payment,
    bank_name="sber"
)
```

### Обработка платежей
Метод `create_order` обрабатывает платежи в зависимости от выбранного типа оплаты:
- **SBP_Payment** требует указания названия банка.
- **CreditCardPayment** требует данных банковской карты.
- **CashPayment** не требует дополнительных данных.

## Доступные классы и методы

### Классы
- `AsotaFacade`: Основной интерфейс для управления пользователями, заказами и товарами на складе.
- `Roles`: Определяет роли пользователей (`trading_agent`, `warehouse_manager`).
- `Product`: Представляет продукты с такими атрибутами, как название и цена.
- `SBP_Payment`, `CreditCardPayment`, `CashPayment`: Обрабатывают платежи в зависимости от метода оплаты.

### Основные методы
- **AsotaFacade.add_user_to_system(role, name)**: Добавляет пользователя с указанной ролью и именем в систему.
- **AsotaFacade.enter_to_system(user)**: Авторизует пользователя в системе.
- **AsotaFacade.add_items_to_warehouse(products)**: Добавляет товары на склад (доступно только для Менеджера склада).
- **AsotaFacade.create_order(product_list, customer_name, amount_from_cust, payment_type, [доп. параметры])**: Создает заказ с указанием списка товаров, имени клиента, суммы и типа оплаты.

## Примечания

- Только пользователи с ролью **Менеджера склада** могут добавлять товары на склад.
- Только пользователи с ролью **Торгового агента** могут создавать и управлять заказами.
- Убедитесь, что пользователи инициализированы с правильными ролями для доступа к соответствующим функциям.

Этот документ описывает основные возможности системы Asota для эффективного использования функционала по обработке заказов и платежей.
