import schedule
import time


def miaFunzione():
    print('Eseguo la mia funzione')


def miaNewFunzione(x: str):
    print(f'funzione con argomenti, {x.upper()}')


# versione wrappata
# @schedule.repeat(schedule.every(10).seconds)
# def funzioneWrappata():
#     return 'funzione schedulata con wrapper'

# Diverse modalità di schedulazione
# schedule.every(2).seconds.do(miaFunzione)
# schedule.every().minute.at(':15').do(miaFunzione)
# schedule.every().day.at('13:22').do(miaFunzione)
# schedule.every().monday.at('09:25').do(miaFunzione)

# versione con ARGOMENTI
# job = schedule.every(2).minutes.do(miaNewFunzione, 'andrea')
# print(schedule.get_jobs())
# schedule.cancel_job(job)

schedule.every(1).seconds.do(miaFunzione)


while True:
    schedule.run_pending()
    time.sleep(1)
