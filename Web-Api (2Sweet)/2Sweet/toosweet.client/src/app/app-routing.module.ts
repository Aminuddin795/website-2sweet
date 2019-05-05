import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent} from './login/login.component';
import { SignupComponent} from './signup/signup.component';
import { FrontpageComponent } from './frontpage/frontpage.component';
import { ProfileComponent } from './profile/profile.component';
import { MessageComponent } from './message/message.component'


const routes: Routes = [
  {path: 'frontpage' , component: FrontpageComponent},
  {path: '', component: LoginComponent},
  {path: 'signup', component: SignupComponent},
  {path: 'profile', component: ProfileComponent},
  {path: 'message', component: MessageComponent},
  
];



@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
