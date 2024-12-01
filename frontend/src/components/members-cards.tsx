import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { ChatType } from '../types/chat';
import { Member } from '../types/members';
import { AlertComponent } from './alert';
import { MemberCard } from './members-card';
import { MembersSearch } from './members-search';

type Props = {
  members: Member[];
  error: Error | null;
  chatInfo: ChatType | undefined;
  loaders: JSX.Element[];
  isLoading: boolean;
  onSearch: (query: string) => void;
  searchQuery: string;
  countMembers: number;
};

export const ChatListMembers: React.FC<Props> = ({
  chatInfo,
  members,
  isLoading,
  error,
  loaders,
  onSearch,
  searchQuery,
  countMembers,
}) => {
  const [alertMessage, setAlertMessage] = useState<string | null>(null);

  const navigate = useNavigate();

  const handleCloseAlert = () => {
    setAlertMessage(null);
  };

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
          {chatInfo?.avatar_url.startsWith('f') ? (
            <div className="members__chat-default">
              <span>{chatInfo.title.charAt(0)}</span>
            </div>
          ) : (
            <img src={chatInfo?.avatar_url} />
          )}

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
          <MemberCard key={member.user.id} chatInfo={chatInfo} member={member} setAlertMessage={setAlertMessage} />
        ))}
      </div>
    </>
  );
};
