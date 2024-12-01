import { useState } from 'react';
import { Link } from 'react-router-dom';
import circleSvg from '../assets/circle-user.svg';
import tg from '../assets/tg.png';
import { Member } from '../types/members';
import { MenuMembers } from './members-menu';

type Props = {
  member: Member;
  setAlertMessage: (string: string | null) => void;
};

export const MemberCard = ({ member, setAlertMessage }: Props) => {
  const [isMenuOpen, setIsMenuOpen] = useState<number | null>(null);

  const toggleMenu = (id: number) => {
    setIsMenuOpen(isMenuOpen === id ? null : id);
  };

  const handleRemoveFromChat = () => {
    setAlertMessage(`Удален из чата`);
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
  return (
    <div
      onClick={() => toggleMenu(member.user.id)}
      className={`members__item ${!member.is_admin ? 'members__item-active' : ''}`}
      style={{ cursor: member.is_admin ? 'default' : 'pointer' }}
      key={member.user.id}>
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <div className="members__avatar">
          {member.user.photo_url !== null ? (
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
  );
};
