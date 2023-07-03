# coding=utf-8

import zAI
from zAI import ztext

zAI.utils.set_backend_key(key_name='MICROSOFT_AZURE_BING_VOICE_API_KEY',key_value='0ba928747403465a85145da9384b6fbd',save=True)

text='파이썬은 배우기 쉽고, 강력한 프로그래밍 언어입니다. 효율적인 자료 구조들과 객체 지향 프로그래밍에 대해 간단하고도 효과적인 접근법을 제공합니다.'
target_text = ztext.zText(text,lang='ko')
target_text.to_voice(backend='Microsoft',outputFile='speech.wav')

import IPython
IPython.display.Audio('speech.wav')

import pygame

pygame.mixer.init()
play = pygame.mixer.Sound('speech.wav')
play.play()

