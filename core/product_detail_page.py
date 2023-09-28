from browser import *

class ProductDetailPage(object):
    add_to_cart = ("#product-addtocart-button", "css selector")
    sizes = (".swatch-option.text", "css selector")
    green_color = ("[option-label='Green']", "css selector")
    cart_count = (".counter-number", "css selector")
    proceed_to_checkout = ("#top-cart-btn-checkout", "css selector")
    product_price = (".price-box .price", "css selector")
    delete_cart = (".action.delete", "css selector")
    delete_popup_ok = (".action-primary.action-accept", "css selector")

    address_0 = ("input[name='street[0]']", "css selector")
    city = ("input[name='city']", "css selector")
    state = ("select[name='region_id']", "css selector")
    zip = ("input[name='postcode']", "css selector")
    country = ("select[name='country_id']", "css selector")
    phone = ("input[name='telephone']", "css selector")
    standard_ship_method = ("input[type='radio'][value='tablerate_bestway']", "css selector")
    next_button = (".button.action.continue.primary", "css selector")
    checkout_button = (".action.primary.checkout", "css selector")
    checkout_price = (".grand.totals .price", "css selector")
    checkout_ship_method = (".shipping-information-content", "css selector")
    confirm_msg = (".page-title .base ", "css selector")

    def select_product_size(driver, size):
        elems = get_elements(driver, ProductDetailPage.sizes)
        for i in elems:
            if i.text == size:
                return i.click()

