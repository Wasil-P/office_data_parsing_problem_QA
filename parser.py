from selenium.webdriver.common.by import By


def parse_offices(driver):
    offices = []

    company_blocks = driver.find_elements(By.XPATH, "//div[contains(@class, 'companydata') "
                                                    "and not(contains(@class, 'contactus_mails_area'))]")

    # Такая реализация цикла призвана создать файл с данными по офисам
    # не зависимо от недостающих данных и\или разницы в блоках
    for block in company_blocks:

        office_data = {}
        full_address_parts = []
        try:
            country = block.find_element(By.XPATH, ".//span[@itemprop='addressLocality']").text
            office_data["Country"] = country
        except:
            pass

        try:
            company_name = block.find_element(By.XPATH, ".//span/following-sibling::span/b").text
            office_data["CompanyName"] = company_name
        except:
            pass

        try:
            street_address = block.find_element(By.XPATH, ".//span[@itemprop='streetAddress']").text
            full_address_parts.append(street_address)
        except:
            pass

        try:
            country_address = block.find_element(By.XPATH, ".//span[@itemprop='addressCountry']").text
            full_address_parts.append(country_address)
        except:
            pass

        try:
            postal_code = block.find_element(By.XPATH, ".//span[@itemprop='postalCode']").text
            full_address_parts.append(postal_code)
        except:
            pass

        try:
            telephone = block.find_element(By.XPATH, ".//span[@itemprop='telephone']").text
            full_address_parts.append(telephone)
        except:
            pass

        if full_address_parts:
            office_data["FullAddress"] = ''.join(full_address_parts)

        if office_data:
            offices.append(office_data)

    return offices
