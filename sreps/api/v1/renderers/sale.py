from rest_framework_csv.renderers import CSVRenderer


class SaleCsvRenderer (CSVRenderer):
    header = [
        'id',
        'quantity',
        'datetime-created',
        'invoice-id',
        'invoice-description',
        'invoice-other-cost',
        'invoice-tax-amount',
        'invoice-is-paid',
        'invoice-datetime-pay-due',
        'invoice-datetime-paid',
        'invoice-datetime-created',
        'invoice-salesperson-id',
        'invoice-salesperson-username',
        'invoice-customer-id',
        'invoice-customer-name',
        'product-id',
        'product-name',
        'product-category',
        'product-lst',
        'product-base-price',
        'product-discount-amount',
        'product-datetime-created',
    ]
