import { Controller, Get, Post, Body, Param, Delete, Patch } from '@nestjs/common';
import { UserService } from './user.service';
import { User } from './shema/user.shema';

@Controller('users')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Get()
  async getAllUsers(): Promise<User[]> {
    return this.userService.findAll();
  }

  @Get(':id')
  async getUserById(@Param('id') id: string): Promise<User> {
    return this.userService.findOneById(id);
  }

  @Post()
  async createUser(@Body() userData: Partial<User>): Promise<User> {
    return this.userService.create(userData);
  }

  @Patch(':id')
  async updateUser(@Param('id') id: string, @Body() updateData: Partial<User>): Promise<User> {
    return this.userService.update(id, updateData);
  }

  @Delete(':id')
  async deleteUser(@Param('id') id: string): Promise<{ message: string }> {
    await this.userService.delete(id);
    return { message: 'User deleted successfully' };
  }
}
