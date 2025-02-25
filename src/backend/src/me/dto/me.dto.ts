// DTO (Data Transfer Object)
import { IsEmail, IsOptional, IsString, MinLength } from 'class-validator';

export class UpdateProfileDto {
  @IsOptional()
  @IsString()
  name?: string;

  @IsOptional()
  @IsEmail()
  email?: string;

  @IsOptional()
  @IsString()
  @MinLength(8, { message: 'The password should have at least 8 characters.' })
  newPassword?: string;

  @IsOptional()
  @IsString()
  confirmPassword?: string;
}