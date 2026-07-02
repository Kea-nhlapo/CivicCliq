import { useState } from 'react';
import { Camera, MapPin, FileText, Loader2 } from 'lucide-react';
import { motion } from 'framer-motion';

export const UploadPanel = ({ onAnalyze }: { onAnalyze: (data: FormData) => void }) => {
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    const formData = new FormData(e.target as HTMLFormElement);
    await onAnalyze(formData);
    setLoading(false);
  };

  return (
    <motion.div 
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="bg-slate-900/50 backdrop-blur-xl border border-white/10 p-8 rounded-3xl shadow-2xl max-w-2xl mx-auto"
    >
      <form onSubmit={handleSubmit} className="space-y-6">
        <div className="border-2 border-dashed border-white/20 rounded-2xl p-10 text-center hover:border-indigo-500 transition-colors cursor-pointer group">
          <input type="file" name="image" className="hidden" id="photo-upload" required />
          <label htmlFor="photo-upload" className="cursor-pointer">
            <Camera className="w-12 h-12 mx-auto text-white/40 group-hover:text-indigo-400 mb-4" />
            <p className="text-white font-medium">Upload incident photo</p>
            <p className="text-white/40 text-sm">PNG, JPG up to 10MB</p>
          </label>
        </div>
        
        <div className="relative">
          <MapPin className="absolute left-4 top-3 text-white/40 w-5 h-5" />
          <input name="location" placeholder="Where is this? (Optional)" className="w-full bg-white/5 border border-white/10 rounded-xl py-3 pl-12 pr-4 text-white focus:outline-none focus:ring-2 focus:ring-indigo-500" />
        </div>

        <button 
          disabled={loading}
          className="w-full bg-gradient-to-r from-indigo-600 to-violet-600 py-4 rounded-xl text-white font-bold hover:shadow-[0_0_20px_rgba(79,70,229,0.4)] transition-all flex items-center justify-center gap-2"
        >
          {loading ? <Loader2 className="animate-spin" /> : "Generate AI Report"}
        </button>
      </form>
    </motion.div>
  );
};
