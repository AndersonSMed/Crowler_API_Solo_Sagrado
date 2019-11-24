from api.celery import app
from bs4 import BeautifulSoup
from cards.serializers import General as CardSerializer

import requests


@app.task
def load_cards():

    num_pagina = 1

    while True:

        url_pagina = "https://www.solosagrado.com.br/categorias/114/Avulso-Portugues/pagina/{}/view/vertical/ord/2/qtdview/36".format(
            num_pagina)

        page = requests.get(url_pagina)

        soup = BeautifulSoup(page.content.decode('utf-8','ignore'), 'html.parser')

        card_items = soup.find_all('div', class_='product_item')

        if card_items is None or len(card_items) == 0:

            break

        for card in card_items:

            card_data = {}

            a_tag = card.find('h5', class_='m_bottom_10').find('a')

            card_data['url_carta'] = "https://www.solosagrado.com.br{}".format(
                a_tag.get('href'))

            card_data['url_imagem_carta'] = 'https://www.solosagrado.com.br/images/produtos/w200/h292/{}'.format(
                card.find('img', class_='tr_all_hover').get('src').split('/')[-1]
            )

            card_data['titulo'] = a_tag.contents[0].strip()

            preco_div = card.find('div', class_='clearfix m_bottom_10')

            card_data['estoque'] = preco_div.find(
                'p', class_='produto-qtd').find('span').contents[0].strip()

            card_data['estoque'] = ''.join(
                [estoque for estoque in card_data['estoque'] if estoque != '\r' and estoque != '\n'])

            card_data['estoque'] = ' '.join(
                [estoque for estoque in card_data['estoque'].split(' ') if len(estoque) > 0])

            card_data['disponivel'] = not 'indisponível' in card_data['estoque'].lower()

            card_data['preco'] = preco_div.find('p', class_='scheme_color f_size_large').find(
                'span', class_='bold').contents[0].strip().split(' ')[-1]

            card_data['preco'] = '.'.join(card_data['preco'].split(','))

            serializer = CardSerializer(data=card_data)

            if serializer.is_valid():

                serializer.save()

        num_pagina += 1
