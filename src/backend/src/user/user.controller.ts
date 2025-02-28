import { Controller, Get, Post, Body, Param, Delete, Patch } from '@nestjs/common';
import { UserService } from './user.service';
import { User } from './shema/user.shema';

@Controller()
export class UserController {
  constructor(private readonly userService: UserService) {}

  // Obtener todos los usuarios
  @Get('/users')
  async getAllUsers(): Promise<User[]> {
    return this.userService.findAll();
  }

  // Obtener un usuario por ID
  @Get('/users/:id')  // Corregido: se debe usar `:id`
  async getUserById(@Param('id') id: string): Promise<User> {
    return this.userService.findOneById(id);
  }

  // Crear un nuevo usuario
  @Post('/users')
  async createUser(@Body() userData: Partial<User>): Promise<User> {
    return this.userService.create(userData);
  }

  // Actualizar un usuario
  @Patch('/users/:id')  // Corregido: agregar `:id` para actualizar un usuario específico
  async updateUser(@Param('id') id: string, @Body() updateData: Partial<User>): Promise<User> {
    return this.userService.update(id, updateData);
  }

  // Eliminar un usuario
  @Delete('/users/:id')  // Corregido: agregar `:id` para eliminar un usuario específico
  async deleteUser(@Param('id') id: string): Promise<{ message: string }> {
    await this.userService.delete(id);
    return { message: 'User deleted successfully' };
  }
}
