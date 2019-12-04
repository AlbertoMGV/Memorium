import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, AlertController, ToastController } from 'ionic-angular';
import { MainPage } from '../';


/**
 * Generated class for the Juego1inPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-juego1in',
  templateUrl: 'juego1in.html',
})
export class Juego1inPage {

  constructor(public navCtrl: NavController, public navParams: NavParams, public alertController: AlertController, public toastCtrl: ToastController,) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad Juego1inPage');
  }

  terminar() {
  	this.navCtrl.popToRoot();
    let toast = this.toastCtrl.create({
        message: 'Tus resultados se han guardado!!!',
        duration: 4000,
        position: 'top'
      });
      toast.present();
  }

  async back() {
    const alert = await this.alertController.create({
      message: '¿Seguro que quieres salir <strong>sin guardar</strong>?',
      buttons: [
        {
          text: 'Cancelar',
          role: 'cancel',
          cssClass: 'secondary',
          handler: (blah) => {
            
          }
        }, {
          text: 'Okay',
          handler: () => {
            this.navCtrl.popToRoot();
          }
        }
      ]
    });

    await alert.present();
  }


}
