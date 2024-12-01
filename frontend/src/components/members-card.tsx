import { useState } from 'react';
import { Link } from 'react-router-dom';
import circleSvg from '../assets/circle-user.svg';
import tg from '../assets/tg.png';
import { ChatType } from '../types/chat';
import { Member } from '../types/members';
import { MenuMembers } from './members-menu';

type Props = {
  member: Member;
  setAlertMessage: (message: string | null) => void;
  chatInfo: ChatType | undefined;
};

export const MemberCard = ({ member, setAlertMessage, chatInfo }: Props) => {
  const [isMenuOpen, setIsMenuOpen] = useState<number | null>(null);

  const toggleMenu = (id: number) => {
    setIsMenuOpen(isMenuOpen === id ? null : id);
  };

  const handleRemoveFromChat = (userId: number, chatId: number | 'all') => {
    if (!chatInfo && chatId !== 'all') {
      setAlertMessage('Ошибка: информация о чате недоступна');
      return;
    }

    const dataToSend = {
      action: 'remove_member',
      user_id: userId,
      chat_id: chatId,
    };

    console.log(JSON.stringify(dataToSend));

    try {
      // Проверка, доступен ли Telegram WebApp API
      if (window.Telegram && window.Telegram.WebApp) {
        const tg = window.Telegram.WebApp;

        // Отправка данных через Telegram WebApp API
        tg.sendData(JSON.stringify(dataToSend));

        // Уведомление о успешной отправке данных
        setAlertMessage(
          chatId === 'all'
            ? `Пользователь удалён из всех чатов`
            : `Пользователь удалён из чата с ID ${chatId}`,
        );
      } else {
        console.error('Telegram WebApp API не доступен');
        setAlertMessage('Telegram WebApp API не доступен');
      }
    } catch (error) {
      console.error('Ошибка при отправке данных:', error);
      setAlertMessage('Не удалось отправить данные. Попробуйте снова.');
    } finally {
      setIsMenuOpen(null);

      setTimeout(() => {
        setAlertMessage(null);
      }, 2000);
    }
  };

  return (
    <div
      onClick={() => toggleMenu(member.user.id)}
      className={`members__item ${!member.is_admin ? 'members__item-active' : ''}`}
      style={{ cursor: member.is_admin ? 'default' : 'pointer' }}
      key={member.user.id}>
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <div className="members__avatar">
          {member.user.photo_url !== null && member.user.photo_url.startsWith('https') ? (
            <img src={member.user.photo_url} alt="Фото пользователя" />
          ) : (
            <img src={circleSvg} alt="Дефолт картинка" />
          )}
        </div>
        <div className="members__data">
          <div className="members__name">
            {member.user.first_name}
            {member.user.is_premium && <img src={tg} alt="Премиум значок" />}
          </div>
          <Link to={`https://t.me/${member.user.username}`}>
            <span className="members__username">@{member.user.username}</span>
          </Link>
        </div>
      </div>
      {member.is_admin && <div className="members__role">админ</div>}

      {isMenuOpen === member.user.id && !member.is_admin && (
        <MenuMembers
          handleRemoveFromChat={() => handleRemoveFromChat(member.user.id, chatInfo?.id || 'all')}
          handleRemoveFromAllChats={() => handleRemoveFromChat(member.user.id, 'all')}
        />
      )}
    </div>
  );
};
