import React from 'react';
import { TelegramLoginButton } from '../components';
import { TelegramUser } from '../types/telegram';

export const LoginTelegramm: React.FC = () => {
  const handleTelegramAuth = (user: TelegramUser) => {
    alert(
      `Logged in as ${user.first_name} ${user.last_name || ''} (ID: ${user.id}${
        user.username ? `, @${user.username}` : ''
      })`,
    );
    console.log('Telegram User:', user);
    // Здесь можно отправить данные пользователя на сервер для валидации
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Авторизация через Telegram</h1>
      <TelegramLoginButton botName="learnpoemsbot" onAuth={handleTelegramAuth} />
    </div>
  );
};
