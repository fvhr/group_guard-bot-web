import React, { useEffect } from 'react';
import { TelegramLoginButtonProps, TelegramUser } from '../types/telegram';

export const TelegramLoginButton: React.FC<TelegramLoginButtonProps> = ({ botName, onAuth }) => {
  useEffect(() => {
    // Добавляем скрипт Telegram виджета
    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://telegram.org/js/telegram-widget.js?22';
    script.setAttribute('data-telegram-login', botName);
    script.setAttribute('data-size', 'large');
    script.setAttribute('data-onauth', 'handleTelegramAuth(user)');
    script.setAttribute('data-request-access', 'write');
    document.getElementById('telegram-button-container')?.appendChild(script);

    // Функция обработки аутентификации
    window.handleTelegramAuth = (user: TelegramUser) => {
      onAuth(user);
    };

    return () => {
      // Удаляем скрипт при размонтировании компонента
      const container = document.getElementById('telegram-button-container');
      if (container) {
        container.innerHTML = '';
      }
    };
  }, [botName, onAuth]);

  return <button id="telegram-button-container">Войти</button>;
};

declare global {
  interface Window {
    handleTelegramAuth: (user: TelegramUser) => void;
  }
}
