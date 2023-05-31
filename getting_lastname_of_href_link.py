import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urlparse




def email_search(useremail):
    url = "https://www.myfitnesspal.com/user/search"

    payload = "utf8=%E2%9C%93&authenticity_token=OL2eSu6%2BzCb%2BdAZ7w7f7fkYiEc4DPAFXISbybPMBDkwmNyaClvVM8iOxLzTUJ4FOaTQYxdmki22OS5NIl%2Ff%2BJQ%3D%3D&username_or_email=" + useremail + "&commit=Search"
    headers = {
        'Host': 'www.myfitnesspal.com',
        'Cookie': 'ajs_anonymous_id=89a62ee0-31e4-4bed-8a95-86cc94316cbf; sp_gam_npa=false; ccpaApplies=true; consentUUID=e014f04b-35a3-4eb4-ab28-d501d852acdb; ccpaUUID=3f84863c-8a9d-403b-8104-c60fc9af1ff3; _gcl_au=1.1.791875102.1680515040; _fbp=fb.1.1680515041709.1833770020; _tt_enable_cookie=1; _ttp=lCJLLMoFg7ogfnYooIytEVJ600z; ccpaConsentAll=true; ccpaReject=false; consentStatus=consentedAll; app-version=4.17.1; __gads=ID=62957e5ca44a8421:T=1680515094:S=ALNI_MaPki3IpbkdUTIp4lNPhJb3rBkWrA; ajs_user_id=164677395746493; _ga=GA1.2.1388484234.1680515094; _gid=GA1.2.235388223.1680515137; p=wHh9PkstSKK14ZvhPxMExWmB; last_login_date=2023-04-04; __gpi=UID=00000bfb980a5764:T=1680515094:RT=1680590663:S=ALNI_MY40GHMKwuY0zN-s4okHjaSxhxzPA; split-id=fe578892-f03c-43f1-949f-1a16b510f3f5; __Host-next-auth.csrf-token=e49ecd88e24aa797dc24de560e7e6b5e3be285017d4684fe83af43248b612045%7Ce6d452bc02d34442c9b64c4e97388c27cc09394de806be6597cba081df0f77d6; dnsDisplayed=false; signedLspa=false; session_event_session_start_forums_164677395746493=true; session_event_session_start_website_164677395746493=true; remember_me=164677395746493%3A7e30ddfc4e6b38e18e5eca1d0a37609f; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.myfitnesspal.com%2Faccount%2Flogin%3Ferror%3Dundefined; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..dzw_SqK8pXAhUJc4.aqtJ4iZLvgGpo5Yp1a4edw2zsG49zmgW2L5GQZKTrE3FQfPmlbr1SLgwbvFyDXNydKuCmAupvmIQfLOixBP7gJbK2IyFwUU3y6kxq3BIlzxV_sGvLYZ0ATJlAnUZvE45ulANDbNC8uNOgjF2d14_qZBzfOiMKchNz1P7FdwK7lbhauySDd5MXxLIDmLoLS1yGM6MM-tpWM4Z1OJtPbnm0ip1l929y652VHPTb8Hprb9jitUI1XNz7SXfSj6eVAeK9oEFwcN37zwMEma8eh2zK5P7IZHPBdeLEpLFv6NAI5H85pnIiXksWvAA6Eqov6emeOjbkt1XZsZ-StowJQthiXxstH6YoIRi1Nbc8qZieCLzLGtNPHRIK7ZeT_RB9kucVk5QVFCvyNzRciIKlPijMO6h89rm4zYeMwkabuDuVhcPHE9-kXr57ukTnbC7AViNhgmqFkZcdapAottbgdMxzxtkSSdj4K0vxHSdjcyM_kKGezJvZlV8eFaNuBTmQvGIEBu3zmWwkiPvILj_2Bc5jxGyWcpbBob4qtRcuzWCC_uu9G_NYh5rxcDJEBADKf1k3wcZ0TKVk7Fqi-ufDPGJ8oEIoSNSoaorlOIDnnZgRe0qNnCabPZckzYMLclXUnlTojr97l0MnAMXjwRmKP-aT6InsbR8hsZEG5Zz-Qz5CHMZbxM5H6rUpbt12QsCKthj9XGKLlLuUSxdZ2kR62yq-t0I3v6lASD7SAPDnnjRDPwXLtRYwdkpfSv0j9ryLGQtmnP4Wuhw4IpST7bzhGbMdNBIyw6qbYfdyDmFC42aIp6RyRHZC6N5mfKfj0B1jGdRTkT53u-lJ6REG3cQTgNn2Qx5p4n1cMsda4TLThoSA8kef3Ru0e5sBXcJK9v_zyRfVgkqgBLzr5tKwo32be16Ebr3daKtiRk_4Vy4c34diqcTVmAmnvaZNAKWghhCGT73AaBpdLS28mAbgXGecgk2MT_N7TRv2JHHsGbuYZ4PPWeivY-fkxF42hDmWz1zTpSIN3ovDd1fcxVBOhMhm_tTZJzHsA.9TxDivEI2l0eaSM4RFimuQ; _dd_s=logs=1&id=5582647e-18cd-4b95-9b34-897ce5531b34&created=1680606687611&expire=1680609119641&rum=0; known_user=217923447; _gat_gtag_UA_273418_104=1; _mfp_session=ZnNBQXVreWg0RStGckdFTGVCOE1WZWNVQnQ2NmJ4MWFSL3VrQjc1ZkpLTytJanVOV1RSTUluVFNjWTBRWFFFZU5zeFRPQ3Q4UzBmTXZWK21ZbHFUTTZCaDJUanhLZ2szdnBYZjREMHY5Yi9hM0R5SmRqOHNZdUdOM0c3bVJid3U1WjVveGhRNEVCTlBlZWpUTnI4Qzd0T21oTWVKR3lkMVdhMTdCaGV6RXJYWDRYNE1ERTBuQmV1SzZsT0RuSGYzb3YyekRpRU9uZldJdDRlUnE0ejVmd2RtQ25yVFdkeWtlOVJjdklMNUNnYUo5SGdtdDNkSlh5OWJZQjhlbkgwbVR6RkVhZ2ZsLzhXQ3N6U2dwalp3N2dtekVGZ2svQldHeW9ueGlZS25FWmUwTU1WOTQ4QXk4dzlRRE9PQ2VRNHJnK3ZKSTFBSERxS3FsMmYxam9uR1Z5MW5zNVFjd2JmWWpUOGN4Zlp6NGhteFF2Q0VldDArVElVcjRNVzdqWUdNclU5OStRd2xmenh3OW5CMnJkcnA3QT09LS1TU0xHLzRUQ3h4N01sSHhranZkOVBRPT0%3D--959943250e4ccf81fbbcb4608ffb1f058cdbbb2a; amplitude_id_2746a27a28431837e776d192ed6db604myfitnesspal.com=eyJkZXZpY2VJZCI6Ijg4NWRiOGI4LTVlODYtNGQxMC05Y2Q5LTc2MWIwMGI5ZWJiMlIiLCJ1c2VySWQiOiIxNjQ2NzczOTU3NDY0OTMiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE2ODA2MDY4MjI1MzEsImxhc3RFdmVudFRpbWUiOjE2ODA2MDgyMzkxMTgsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==; __Host-next-auth.csrf-token=32f2ee20ee9bdc9fb001109791f8cf3a2a408fb083c249017828188ea391dd2a%7C25a607ebd8a6486b690269873839fd05d15a577338e40d6e0095329cf7e911a7; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.myfitnesspal.com%2Faccount%2Flogin%3Ferror%3Dundefined; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..omUQTnHM8S1OzYum.tvQxM7yyGhElZ_tMRR1lrVfjIrW7-UqKAo2nuiP-egZP_4Ul6oaLJKwA12ZNqhkW9v8NlzO9q75o6mM2RCqGDiSBXBHvokHjFQWpwZZW2LxfgPXsu1Ju4RDzfS-jmUPTgkVWfXE3eg9WSBm6VqmAIVCwBW6dbsi14V6hC08VlQb2wRGrhNqshY_bBRQQSuoDmP_zD3wEw3141iCLvyFZWLC1K0-eZXGeb30U2Y-xTNfdJwR0dHt_9qUafSTHJoGAo59zEt2EnZDgy95Fb-D1a_o9-5QwZbXq_e7ZSXO14V2NcjlrwRE9r71y4coYza5DHfU0Q5s0uIZd03ubyV2fUbTx-UC6TyFu3COjEONAxolQ0kDtF6z5qCLiZXZCoGLQsgJ2AQLF6uq8nOr7q_PCa7rzp63t6VBZ2bPEjNLZd0f9BMUc2Umej0_CrUzT_da0f9_0dDFh8C0k0tOvZl1CRlthDcPWBA4NzNXGUFzuPDXL-8fkPKQ_wx63FwO4exvIqBWkPRCTzZHqRPfm1jhKg2j0YOhiXz4etDXavVWXF3KD64LGmABdF-UTNC184U4u_9Arq91Wlsb8-0-n8ZUBZrjMRSZ11nH1jlfxTqFPrCHdJSGqx3EG8FE_YUCjLqNlFHATKdNOTgrjqMLJKPwwFvCbrkxeElmSXR-uw2NttKIfpWOKJKmEizkUt_kqKXziAHBd6QhI-u7CfW4Qj0ik5zy6Dkb8JdsEDxX0CkIYB9-EaF0e4L6lWYqoju1uQnbWK9o8BpTLWZVu4hBzk3_665LXL3-5z5d4y8VcXS4RH_-pE3DpqNXFRBy5oP-DMi-B9VJZas0QxtHY9cESrvk5MW3uqDq3G4xHl8MAauFYjcNjVzX7Ml1kALx0s25FyKIdohr4cnE2jOueTtaxJUofGcpvAshQtmUFkspFXkq2U8Hm9jPS-4WJlrv01AB9gLqrX1SRynEW67dDQTslkeA_5PcB93Xu-GTAV9w5RilyEX07n2u-FI25yoWhmO4S-5xK2b430bg_OnmnuPa6S2yCyELaYg.PynKs-MlFrlfXkqrcOkMGQ; _mfp_session=OWcvc3BMYWdVQTZxYU1tcU9Ga0RkRUhlMVV3ekpSK05qWkxiUWxoOEJaNkpKY0NSenZoMWRxSklrWGRaZ3ZIMHBxcFdyTUtlTkJRQ0I3SitkVE0yN0dFNUVvZzBoQXd4cER1MmwvakZzYjFWdVRjWEtnaWdqdXUxdXVkOWV5bzdSZXRzQ3owemh2OVN2UFFjYlpNbVd6QmxDU1dCKzJqczF1dFRPOXpuR1ZFU25JaGhsYzA1bWZpOFNHbFd4YlptLys5UWZRcGFpdE4wSjFBY3NLNUtYUTRvaUV6WXYycjROT3k4YVRTSEIxa2U0N1lyMUdmVEQvdE9FNWpWT1IzZDBrQzdJZjVGTDF3UmNwWDdBT2hWVEhUYVoxZnY2UzlvRlMzUzZvNGJGZHZQd0VHU212Yy8wNTNrZVREU2ltV01SSWJyQVlmNmNGRHBYZXBYMnMvSjZ0THVoWWE3Ymw1STBwZ2d0emNFWHZvT0FVRGJValJvWVRIU29Qa1dPK0FIRmFOSU9xNkg0U0xGQXNUZUdva0VxZz09LS1yakxLLzFEMGxuNStTb2QwTkhYa3lBPT0%3D--ca86243050267ace5cf2b56e5f118be544dcfcf2; app-version=4.17.1; known_user=217923447; last_login_date=2023-04-06; p=wHh9PkstSKK14ZvhPxMExWmB; remember_me=164677395746493%3A09f33da0e95a55821c36f8d24a4b99d0; split-id=e7c0b6c5-aabb-4ada-8149-8a100ec6661e',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://www.myfitnesspal.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; SM-G977N Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'X-Requested-With': 'com.android.browser',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://www.myfitnesspal.com/user/search',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    resp_email = response.text
    soup = BeautifulSoup(resp_email, 'html.parser')
    # print(soup)
    links = soup.find_all("link")
    for link in links:
        if 'https://www.myfitnesspal.com' in str(link):
            parsed_url = urlparse(link['href'])
            last_word = parsed_url.path.split('/')[-1]
            return last_word
            break
    # print(link)

useremail = "waleed@gmail.com"
resp_username = email_search(useremail)
print("USER Name :::", resp_username)
