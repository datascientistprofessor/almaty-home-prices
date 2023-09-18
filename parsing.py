import requests
from bs4 import BeautifulSoup
import unidecode
from time import sleep

headers  = {"User-Agent":
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729"}

def array():
    for count in range(2, 539):
        sleep(5)

        url = f'https://krisha.kz/prodazha/doma/almaty/?page={count}'

        response = requests.get(url, verify=False)

        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all('div', class_='a-card a-storage-live ddl_product ddl_product_link is-colored paid-color-light-red is-visible') #find_all
        data1 = soup.find_all('div', class_='a-card a-storage-live ddl_product ddl_product_link is-colored paid-color-light-red is-visible is-urgent') #find_all
        data2 = soup.find_all('div', class_='a-card a-storage-live ddl_product ddl_product_link is-colored paid-color-light-green is-visible is-urgent')
        data3 = soup.find_all('div', class_='a-card a-storage-live ddl_product ddl_product_link is-colored paid-color-light-green is-visible')
        data4 = soup.find_all('div', class_='a-card a-storage-live ddl_product ddl_product_link not-colored is-visible is-urgent')
        data5 = soup.find_all('div', class_='a-card a-storage-live ddl_product ddl_product_link not-colored is-visible')

        for i in data1:
            data.append(i)
        for i in data2:
            data.append(i)
        for i in data3:
            data.append(i)
        for i in data4:
            data.append(i)
        for i in data5:
            data.append(i)

        list_location = ['Alatau district', 'Almaly district', 'Bostandyk district', 'Zhetysu district', 'Medeu district', 'Nauryzbay district', 'Turksibsky district',
                         'Auezovsky district', 'other']
        list_location_ru = ['Алатауский р-н', 'Алмалинский р-н', 'Бостандыкский р-н', 'Жетысуский р-н', 'Медеуский р-н', 'Наурызбайский р-н', 'Турксибский р-н', 'Ауэзовский р-н']

        for i in data:
            room_sqm = i.find('a', class_='a-card__title').get_text().strip().split(',')
            room = room_sqm[0].split('-')[0]
            sqm = room_sqm[1].strip().split(' м')[0]

            price = i.find('div', class_='a-card__price').get_text().strip()
            price = price.replace(u'\xa0', u' ')
            price = price.split(' 〒')[0].replace(' ', '')

            floor_year = i.find('div', class_='a-card__text-preview').get_text().strip()

            try:
                if 'этаж' not in floor_year and ' г.п' in floor_year :
                    floor = None
                    year = floor_year.split(' г.п')[0]
                elif 'этаж' in floor_year and ' г.п' not in floor_year :
                    floor = floor_year.split(' этаж')[0]
                    year = None
                elif 'этаж' not in floor_year and ' г.п' not in floor_year :
                    floor = None
                    year = None
                else:
                    floor = floor_year.split(' этаж')[0]
                    year = floor_year.split(' г.п')[0].split(',')[1].strip()
            except IndexError:
                floor = None
                year = None

            location = i.find('div', class_='a-card__subtitle').get_text().strip()

            if list_location_ru[0] in location:
                location = list_location[0]
            elif list_location_ru[1] in location:
                location = list_location[1]
            elif list_location_ru[2] in location:
                location = list_location[2]
            elif list_location_ru[3] in location:
                location = list_location[3]
            elif list_location_ru[4] in location:
                location = list_location[4]
            elif list_location_ru[5] in location:
                location = list_location[5]
            elif list_location_ru[6] in location:
                location = list_location[6]
            elif list_location_ru[7] in location:
                location = list_location[7]
            else:
                location = list_location[8]

            yield room, sqm, floor, year, location, price

