import { Controller, Get, Patch, Req, Body, UseGuards } from '@nestjs/common';
import { MeService } from './me.service';
import { UpdateProfileDto } from './dto/me.dto';
import { AuthGuard } from '@nestjs/passport';

@Controller('me')
@UseGuards(AuthGuard('jwt'))
export class MeController {
  constructor(private readonly userService: MeService) {}

  @Get()
  getProfile(@Req() req) {
    return this.userService.getProfile(req.user);
  }

  @Patch()
  updateProfile(@Req() req, @Body() updateProfileDto: UpdateProfileDto) {
    return this.userService.updateProfile(req.user, updateProfileDto);
  }
}