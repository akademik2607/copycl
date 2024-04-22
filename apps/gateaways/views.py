from django.shortcuts import render
import requests
import base64

def show_payd_card_form(request):

    return render(request, 'gateaways/pay_card_data_form.html', context={})


def checkout(request):
    pass
    # print(dir(request))
    # if request.method != 'POST':
    #     response = requests.post(
    #         # 'https://api.cloudpayments.ru/test',
    #         'https://api.cloudpayments.ru/payments/cards/charge',
    #
    #         headers={
    #             'Accept': 'application/json',
    #             'Content-Type': 'application/json',
    #             'Authorization': 'Basic ' + base64.b64decode("$publicID:$apiKey", 'utf-8'),
    #         },
    #         data= {
    #             'Amount': amount,
    #             'Currency': 'RUB',
    #             'InvoiceId': order_id,
    #             'IpAddress': ip,
    #             'CardCryptogramPacket': token,
    #             'CultureName': 'ru-RU',
    #             'Payer': {
    #                 'FirstName': 'first_name'
    #             }
    #         }
    #     )




        # CultureName' = > 'en-US',
        #   'Payer' = > array('FirstName' = > $_POST['first_name']
        #     'FirstName' = > $_POST['first_name']
        # $response = wp_remote_post(
        #             // 'https://api.cloudpayments.ru/test',
        #             'https://api.cloudpayments.ru/payments/cards/charge',
        #             array(
        #                 'method' = > 'POST',
        #                  'timeout' = > 45,
        #                   'headers' = > array(
        #                        'Accept' = > 'application/json',
        #                          'Content-Type' = > 'application/json',
        #                           'Authorization' = > 'Basic '.base64_encode("$publicID:$apiKey"),
        # ),
        # 'body' = > json_encode(
        #     array(
        #         'Amount' = > $amount,
        #                       'Currency' = > 'USD',
        #                                      'InvoiceId' = > $order_id,
        #                                                       'IpAddress' = > $ip,
        #                                                                        'CardCryptogramPacket' = > $_POST[
        #                                                                                                        'token'],
        #                                                                                                    'CultureName' = > 'en-US',
        #                                                                                                                      'Payer' = > array(
        #     'FirstName' = > $_POST['first_name']
        # )
        # )
        # )
        # )
        # );
        #
        # // добавляем
        # проверки, что
        # запрос
        # не
        # улетел
        # в
        # ошибку
        # if (is_wp_error( $response) | | 'OK' !== wp_remote_retrieve_response_message( $response ) ) {
        # // обрабатываем ошибку
        # }
        #
        # // не
        # ошибка? продолжаем
        # $body = json_decode(wp_remote_retrieve_body( $response ), true );
        #
        # // это
        # обработка
        # 3 - D
        # Secure
        # if (false == $body['Success']) {
        #
        # $MD = isset( $body['Model']['TransactionId'] ) & & $body['Model']['TransactionId'] ? $body['Model']['TransactionId']: false;
        # $
        #     PaReq = isset( $body['Model']['PaReq'] ) & & $body['Model']['PaReq'] ? $body['Model']['PaReq']: false;
        # $AcsUrl = isset( $body['Model']['AcsUrl'] ) & & $body['Model']['AcsUrl'] ? $body['Model']['AcsUrl']: false;
        #
        # if ($AcsUrl & & $PaReq) {
        #
        # // формируем HTML форму прямо тут! и редиректим!
        # echo '<p>Редиректим...</p><form id="process3d" action="'.esc_url( $AcsUrl ).'" method="POST">
        # < input type="hidden" name="MD" value="' . absint( $MD ) . '" >
        # < input type="hidden" name="PaReq" value="' . esc_attr( $PaReq ) . '" >
        # < input type="hidden" name="TermUrl" value="http://урл-на-вашем-сайте/3ds.php" >
        # < / form >
        # < script type="text/javascript" >
        # document.getElementById( \'process3d\' ).submit();
        # < / script > ';
        # exit;
        # }
        #
        # // всё ещё тут? значит какая-то ошибка и тут вам надо её обработать
        #
        # }
        #
        # // всё ещё тут? продолжаем!
        # if ( true == $body['Success'] ) {
        # // Ура! оплата прошла, делаем то, что нужно
        # }
