import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';

interface PhoneFormInput {
  sms: string;
}

export const FormSms: React.FC = () => {
  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm<PhoneFormInput>();

  const [sms, setSms] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const navigate = useNavigate();

  const handleInput = (event: React.ChangeEvent<HTMLInputElement>) => {
    const value = event.target.value.replace(/\D/g, '');

    if (value.length <= 4) {
      setSms(value);
      setValue('sms', value);
    }
  };

  const onSubmit = (data: PhoneFormInput) => {
    console.log('Submitted SMS code:', data.sms);
    navigate('/chats');

    setIsLoading(true);

    setTimeout(() => {
      setIsLoading(false);
    }, 1000);
  };

  return (
    <div className="form form__login">
      <div className="form__title">Авторизация</div>

      <form onSubmit={handleSubmit(onSubmit)} className="form__block" autoComplete="off">
        <div className="form-inputs">
          <label htmlFor="sms">СМС - код</label>
          <input
            id="sms"
            type="text"
            value={sms}
            {...register('sms', { required: 'Введите код', maxLength: 4 })}
            onChange={handleInput}
            className={`sms-input ${errors.sms ? 'error' : ''}`}
          />
          {errors.sms && <p className="error-message">{errors.sms.message}</p>}
        </div>

        <button
          type="submit"
          className={`sms-button ${sms.length === 4 ? 'active' : ''}`}
          disabled={sms.length !== 4 || isLoading}>
          {isLoading ? 'Загрузка...' : 'Войти'}
        </button>
      </form>
    </div>
  );
};
