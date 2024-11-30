import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import circleSvg from '../assets/circle-user.svg';
import tg from '../assets/tg.png';
import { ChatType } from '../types/chat';
import { Member } from '../types/members';
import { AlertComponent } from './alert';
import { MenuMembers } from './members-menu';
import { MembersSearch } from './members-search';

type Props = {
  members: Member[];
  error: Error | null;
  chatInfo: ChatType | undefined;
  loaders: JSX.Element[];
  isLoading: boolean;
  onSearch: (query: string) => void;
  searchQuery: string;
	countMembers: number
};

export const ChatListMembers: React.FC<Props> = ({
  chatInfo,
  members,
  isLoading,
  error,
  loaders,
  onSearch,
  searchQuery,
	countMembers
}) => {
  const [isMenuOpen, setIsMenuOpen] = useState<number | null>(null);
  const [alertMessage, setAlertMessage] = useState<string | null>(null);

  const navigate = useNavigate();

  const toggleMenu = (id: number) => {
    setIsMenuOpen(isMenuOpen === id ? null : id);
  };

  const handleRemoveFromChat = () => {
    setAlertMessage(`Удален из чата ${chatInfo?.title}`);
    setIsMenuOpen(null);

    setTimeout(() => {
      setAlertMessage(null);
    }, 1000);
  };

  const handleRemoveFromAllChats = () => {
    setAlertMessage('Удален из всех чатов');
    setIsMenuOpen(null);

    setTimeout(() => {
      setAlertMessage(null);
    }, 2000);
  };

  const handleCloseAlert = () => {
    setAlertMessage(null);
  };
	console.log(alertMessage);
	
  return (
    <>
      {alertMessage && (
        <AlertComponent handleCloseAlert={handleCloseAlert} alertMessage={alertMessage} />
      )}
      <div className="members__header">
        <div onClick={() => navigate('/chats')} className="members__back">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="32"
            height="32"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            className="lucide lucide-undo-2">
            <path d="M9 14 4 9l5-5" />
            <path d="M4 9h10.5a5.5 5.5 0 0 1 5.5 5.5a5.5 5.5 0 0 1-5.5 5.5H11" />
          </svg>
          <div className="members__back-text">Назад</div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
          <img src={chatInfo?.avatar_url} alt="Chat" />
          <div className="members__chat-image">
            <div>{chatInfo?.title}</div>
            <span>{countMembers} участников</span>
          </div>
        </div>
      </div>
      <MembersSearch onSearch={onSearch} searchTerm={searchQuery} />

      {error && <p className="members__error">Error: {error.message}</p>}

      <div className="members__list">
        {isLoading && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>{loaders}</div>
        )}
        {members.length === 0 && !isLoading && (
          <div className="members__none">
            {' '}
            <div style={{ fontSize: '2.3rem' }}>😞</div>
            <div>Нет результатов</div>
          </div>
        )}
        {members.map((member) => (
          <div
            onClick={() => toggleMenu(member.user.id)}
            className={`members__item ${!member.is_admin ? 'members__item-active' : ''}`}
            style={{ cursor: member.is_admin ? 'default' : 'pointer' }}
            key={member.user.id}>
            <div style={{ display: 'flex', alignItems: 'center' }}>
              <div className="members__avatar">
                {member.user.photo_url.startsWith('https') ? (
                  <img src={member.user.photo_url} />
                ) : (
                  <img src={circleSvg} alt="Дефолт картинка" />
                )}
              </div>
              <div className="members__data">
                <div className="members__name">
                  {member.user.first_name}
                  {member.user.is_premium && <img src={tg} alt="" />}
                </div>
                <Link to={`https://t.me/${member.user.username}`}>
                  <span className="members__username">@{member.user.username}</span>
                </Link>
              </div>
            </div>
            {member.is_admin && <div className="members__role">админ</div>}

            {isMenuOpen === member.user.id && !member.is_admin && (
              <MenuMembers
                handleRemoveFromChat={handleRemoveFromChat}
                handleRemoveFromAllChats={handleRemoveFromAllChats}
              />
            )}
          </div>
        ))}
      </div>
    </>
  );
};
